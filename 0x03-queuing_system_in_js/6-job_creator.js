import kue from "kue";

// Create a job queue
const queue = kue.createQueue();

// Define job data
const jobData = {
  phoneNumber: "4153518780",
  message: "Hello! This is a push notification.",
};

// Create job
const job = queue.create('push_notification_code',
  jobData).save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    } else {
      console.log(`Failed to create job: ${err}`);
    }
  });

// Handle job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Handle job failure
job.on('failed', () => {
  console.log('Notification job failed');
});
