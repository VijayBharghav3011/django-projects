var item_is_active = null;

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();

            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

toDoList();

async function toDoList() {
    const item_list = document.querySelector('.item_list_pending');
    const item_lst_completed = document.querySelector('.item_list_completed');
    item_list.innerHTML = '';
    item_lst_completed.innerHTML = '';

    let pending = 0;
    let complete = 0;

    const url = `/task-list/`;

    try {
        const response = await fetch(url);
        console.log(response);

        if (!response.ok) {
            document.querySelector('.completed_block').style.display =   'none';
            document.querySelector('.pending_block').style.display =   'none';
            throw new Error('Network response was not ok ' + response.statusText);
        }
        const data = await response.json();

        data.forEach((task) => {
            const listItem = document.createElement('div');
            listItem.classList.add('list_item');

            if (task.completed) {
                complete += 1;
                listItem.innerHTML = `
                    <div class="item_title"><s class="item_titles">${task.title}</s></div>
                    <div class="edit">Edit</div>
                    <div class="delete">Delete</div>
                `;
                item_lst_completed.appendChild(listItem);
            } else {
                pending += 1;
                listItem.innerHTML = `
                    <div class="item_title"><span class="item_titles">${task.title}</span></div>
                    <div class="edit">Edit</div>
                    <div class="delete">Delete</div>
                `;
                item_list.appendChild(listItem);
            }

            let edit_btn = listItem.querySelector('.edit');
            edit_btn.addEventListener('click', () => editItems(task));

            let delete_btn = listItem.querySelector('.delete');
            delete_btn.addEventListener('click', () => deleteItem(task));

            let titles = listItem.querySelector('.item_titles');
            titles.addEventListener('click', () => strikeItem(task));
        });

        const completeList= document.querySelector('.completed_block');
        const pendingList = document.querySelector('.pending_block');
        console.log(complete);

        complete === 0 ?completeList.style.display = 'none' : completeList.style.display = 'block';
        pending === 0 ? pendingList.style.display =  'none' : pendingList.style.display = 'block';


    } catch (error) {
        console.error('There has been a problem with your fetch operation:', error);
    }
}



let form = document.querySelector('#form');
form.addEventListener('submit', async(e) => {
    e.preventDefault();
    var url = '/create-task/';

    if (item_is_active != null) {
       url = `/update-task/${item_is_active.id}`;
    }
    const title = document.querySelector('#title').value;
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'title': title,
                'completed': false,
            })
        })
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        item_is_active = null;
        document.querySelector('#form').reset();
        toDoList();
    }
    catch(error) {
        console.error('Error in posting task:', error);
    }
});

function editItems(item) {
    const title = document.querySelector('#title');
    item_is_active = item;
    title.value = item_is_active.title;

}

async function deleteItem(item) {
    const confirm = window.confirm(`Are you sure you want to delete the task ${item.title}`)
    if(!confirm) {
        return
    }
    const title = document.querySelector('#title');
    item_is_active = item;
    title.value = item_is_active.title;

    const url = `/delete-task/${item_is_active.id}`;

    try {
        const response = await fetch(url, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        item_is_active = null;
        document.querySelector('#form').reset();
        toDoList();
    }
    catch(error) {
        console.error('Error in Deleting task:', error);
    }
}

async function strikeItem(item) {
    let check_completed_status = item.completed;
    check_completed_status = !check_completed_status;

    const url = `/update-task/${item.id}`;
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },

            body: JSON.stringify({
                 'title': item.title,
                 'completed': check_completed_status,
            })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        item_is_active = null;
        document.querySelector('#form').reset();
        toDoList();
    }
    catch(error) {
        console.error('Error in posting task:', error);
    }
}
