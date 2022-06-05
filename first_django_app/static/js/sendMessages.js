let json = '';


/**
 * Send Message
 * @param {*} token is the csrf_middlewaretoken created in template with django syntax
 */

async function sendMessage(token, username) {
    const url = window.location.href;

    const last = url.split("/")

    console.log(last[last.length - 2]);
    currentChat = last[last.length - 2];
    event.preventDefault();
    let fd = new FormData();
    document.getElementById('loading').classList.remove('d-none');
    fd.append('textmessage', messagefield.value);
    fd.append('csrfmiddlewaretoken', token);
    messagefield.value = '';
    try {
        instantMessage(username);
        let response = await fetch(`/chat/${currentChat}/`, {
            method: 'POST',
            body: fd
        });
        console.log('response is', response)
        let gotFromServer = await response.json();
        json = JSON.parse(gotFromServer);
        console.log('mit json is', gotFromServer)
        console.log('mit parse is', json)
        document.getElementById('deleteMessage').remove();
        serverMessage(username);
        document.getElementById('loading').classList.add('d-none')
    } catch (e) {
        errorMessage();
    }
}


/**
 * Instant message created with JS
 * @param {*} username is the request.user.username created in template with django syntax
 */

function instantMessage(username) {
    messageContainer.innerHTML += ` <div id="deleteMessage" class="message-container">
            <div style="padding:8px;"><span class="color-grey">[${createDate()}]</span>  ${username}: <p><i style="word-break: break-all;" class="color-grey">${messagefield.value}</i></p>
             ><img class="hooks" src="/static/img/check.png"></div></div>`;
}


/**
 * Instant message will be delated in main function and replaced with message from database
 * @param {*} username is the request.user.username created in template with django syntax
 */

function serverMessage(username) {
    messageContainer.innerHTML += ` <div class="message-container">
            <div style="padding:8px;"><span>[${createDateFromServer(json.fields.created_at)}]</span>  ${username}: <p><i style="word-break: break-all;">${json.fields.text}</i></p>
             <img class="hooks" src="/static/img/check.png"><img class="hooks" src="/static/img/check.png"></div></div>`;


}


// if error occurs give user feedback in form of a text message
function errorMessage() {
    document.getElementById('deleteMessage').remove();
    messageContainer.innerHTML += ` <div>
             <span style="color:red"> There went something wrong, please try again later.</span>
             </div>`;
}