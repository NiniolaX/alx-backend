import { expect } from "chai";
import kue from "kue";
import createPushNotificationsJobs from "./8-job";
import sinon from 'sinon';

// Unittest for createPushNotificationsJobs function
describe('createPushNotificationsJobs', () => {
    let queue;

    before(() => {
        queue = kue.createQueue(); // Create new queue instance
        queue.testMode.enter(); // Enter test mode
    })

    afterEach(() => {
        queue.testMode.clear(); // Clear all queued jobs
    });

    after(() => {
        queue.testMode.exit(); // Exit test mode
    });

    it('display an error message if jobs is not an array', () => {
        const fakeJobArray = { name: 'Not an array' };
        const badFn = () => createPushNotificationsJobs(fakeJobArray, queue);
        expect(badFn).to.throw(Error, /Jobs is not an array/);
    });

    it('creates two new jobs on queue', () => {
        const jobsData = [
            { phoneNumber: '4153818782', message: 'This is the code 4321 to verify your account' },
            { phoneNumber: '4154318781', message: 'This is the code 4562 to verify your account' },
        ]

        createPushNotificationsJobs(jobsData, queue);

        // Validate number of jobs added to queue
        expect(queue.testMode.jobs.length).to.equal(jobsData.length);

        // Validate job type
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');

        // Validate job data
        expect(queue.testMode.jobs[0].data).to.deep.equal(jobsData[0]);
        expect(queue.testMode.jobs[1].data).to.deep.equal(jobsData[1]);
    });

    it('logs message to console on job creation', () => {
        const consoleLogSpy = sinon.spy(console.log);

        createPushNotificationsJobs([{ phoneNumber: '4153818782', message: 'This is the code 4321 to verify your account' }], queue);

        expect(consoleLogSpy.calledWith('Notification job created: 1')).to.be.true;
    });
});
