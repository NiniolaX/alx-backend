/**
 * Creates jobs in a Kue queue
 * 
 * Creates jobs in a Kue queue, logs a message when job creation succeeds or fails. It handles job events 'complete', 'failed' and 'progress'.
 * 
 * Args:
 *    jobs - And array of job data
 *    queue - A Kue queue
 * Returns: None
 * Raises: Error when 'jobs' is not an array
*/
function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData).save((err) => {
      if (err) {
        console.log('Notification job not created')
      } else {
        console.log(`Notification job created: ${job.id}`);
      }
    });

    // Handle job events
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    }).on('failed', (err) => {
        console.log(`Notification job ${job.id} failed: ${err}`);
    }).on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
    })
  });
}

export default createPushNotificationsJobs;
