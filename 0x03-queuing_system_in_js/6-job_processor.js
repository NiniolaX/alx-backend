import kue from "kue";

// Create queue
const queue = kue.createQueue();

// Send notification function
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber} with message: ${message}`);
};

// Process listens to new jobs on 'push_notification_code'
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);

  // Call done when finished
  done();
});
