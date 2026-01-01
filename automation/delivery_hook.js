/**

Automates the handover from Designer to Video Editor.

Triggers a notification when the final PSD/PNG is uploaded. */

const axios = require('axios');

async function notifyTeam(thumbnailUrl, videoTitle) { const slackWebhook = process.env.SLACK_WEBHOOK;

await axios.post(slackWebhook, {
    text: `🎨 *New Thumbnail Ready:* ${videoTitle}\nView here: ${thumbnailUrl}`,
    attachments: [{
        image_url: thumbnailUrl,
        text: "Does this build enough curiosity? React with 👍 to approve."
    }]
});


}