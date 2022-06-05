function scrollToBottom() {
    end.scrollIntoView()
}

function scrollToTop() {
    start.scrollIntoView()
}





//open dialog to create a new channel

function openDialog() {

    let dialog = document.querySelector('dialog');
    if (!dialog.showModal) {
        dialogPolyfill.registerDialog(dialog);
    }
    dialog.showModal();
    dialog.querySelector('.close').addEventListener('click', function() {
        dialog.close();
    });
}

/**
 * Create new Channel, clear value and close it after creating
 * @param {*} token is the csrf_middlewaretoken created in template with django syntax
 */
function createNewChannel(token) {
    let dialog = document.querySelector('dialog');
    newChannel = document.getElementById('newChatRoom')
    createChannelInDatabase(newChannel.value, token)
    newChannel.value = '';
    dialog.close();
}

//save the new channel in database
async function createChannelInDatabase(channel, token) {
    let fd = new FormData();
    fd.append('csrfmiddlewaretoken', token)
    fd.append('chat', channel)
    fd.append('slug', channel)
    try {
        let response = await fetch('/chat/', {
            method: 'POST',
            body: fd

        })
        console.log('response is', response)
        let gotFromServer = await response.json();
        json = JSON.parse(gotFromServer);
        console.log('mit json is', gotFromServer)
        console.log('mit parse is', json)
        let chatrooms = document.getElementById('chatrooms')
        chatrooms.innerHTML += `<a class="mdl-navigation__link" href="/chat/${json.fields.name}/">${json.fields.name}</a>`;

    } catch (e) {
        console.error(e);
    }
    window.addEventListener('click', () => {
        window.location = ('/chat/')
    })
}