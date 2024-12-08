import express from "express";
import redis, { createClient} from 'redis';
import { promisify } from 'util';

// Create the Redis client
const client = createClient();

// Promisify Redis methods for asynchronous usage
const clientGetAsync = promisify(client.get).bind(client);
const clientSetAsync = promisify(client.set).bind(client);

// List of products
const listProducts = [
    { id: 1, name: "Suitcase 250", price: 50, stock: 4, },
    { id: 2, name: "Suitcase 450", price: 100, stock: 10, },
    { id: 3, name: "Suitcase 650", price: 350, stock: 2, },
    { id: 4, name: "Suitcase 1050", price: 550, stock: 5, },
];

// Function to retrieve product by ID
function getItemById(itemId) {
    return listProducts.find(item => item.id === itemId);
};

// Function to reserve stock of a product by its ID
async function reserveStockById(itemId, stock) {
    return await clientSetAsync(`item.${itemId}`, stock, redis.print);
}

// Function to get reserved stock of a product by its ID
async function getCurrentReservedStockById(itemId) {
    const stock = await clientGetAsync(`item.${itemId}`);
    if (!stock) {
        return 0; // If no stock is found
    } else {
        return parseInt(stock, 10);
    }
};

// Function to format product
function formatProduct(product) {
    const formattedProduct = {
        itemId: product.id,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock,
    };
    return formattedProduct;
};

// Create server
const app = express();
const port = 1245;

app.get('/list_products', (req, res) => {
  res.send(
        listProducts.map(product => formatProduct(product)));
});

app.get('/list_products/:itemId', (req, res) => {
    // Get item ID for query parameters
    const { itemId } = req.params;
    // Check that item ID was provided
    if (!itemId) {
        res.send({"status": "No item id provided"});
    }

    // Retrieve item from product list by ID
    const item = getItemById(parseInt(itemId));
    // Return Not found message if item is not found
    if (!item) {
        res.send({"status": "Product not found"});
    }

    // Calculate available stock and return item
    getCurrentReservedStockById(itemId)
        .then((reservedStock) => {
            const formattedItem = formatProduct(item);
            formattedItem["currentQuantity"] = item.stock - parseInt(reservedStock);

            // Send data
            res.send(formattedItem);
        }).catch((err) => {
            res.status(500).send({"status": err.message});
        });
});

async function handleReservation(req, res) {
    // Get item ID for query parameters
    const { itemId } = req.params;
    // Check that item ID was provided
    if (!itemId) {
        res.send({"status": "No item id provided"});
    }

    // Retrieve product from product list by ID
    const item = getItemById(parseInt(itemId));
    // Return 404 error if product is not found
    if (!item) {
        res.send({"status": "Product not found"});
    }

    // Get quantity of reserved stock
    try {
        const reservedStock = await getCurrentReservedStockById(itemId);

        // Check there is stock available before reservation
        const availableStock = item.stock - parseInt(reservedStock);
        if (availableStock < 1) {
            res.send({"status": "Not enough stock available", "itemId": itemId});
        }

        await reserveStockById(itemId, reservedStock + 1);
        res.send({"status": "Reservation confirmed", "itemId": itemId});
    } catch (err) {
        res.status(500).send({"status": err});
    }
}

app.get('/reserve_product/:itemId', (req, res) => {
    handleReservation(res, req);
});

app.listen(port, () => console.log(`Server running on http://localhost:${port}`));
