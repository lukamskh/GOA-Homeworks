document.addEventListener('DOMContentLoaded', () => {
    const taskInput = document.getElementById('taskInput');
    const addButton = document.getElementById('addButton');
    const clearButton = document.getElementById('clearButton');
    const taskList = document.getElementById('taskList');

    addButton.addEventListener('click', () => {
        const taskText = taskInput.value.trim();
        if (taskText) {
            const listItem = document.createElement('li');
            listItem.textContent = taskText;
            const editButton = document.createElement('button');
            editButton.textContent = 'Edit';
            editButton.onclick = () => editTask(listItem);
            listItem.appendChild(editButton);
            const deleteButton = document.createElement('button');
            deleteButton.textContent = 'Delete';
            deleteButton.onclick = () => {
                taskList.removeChild(listItem);
            };
            listItem.appendChild(deleteButton);

            taskList.appendChild(listItem);
            taskInput.value = '';
        }
    });

    clearButton.addEventListener('click', () => {
        while (taskList.firstChild) {
            taskList.removeChild(taskList.firstChild);
        }
    });
});

function editTask(listItem) {
    const currentText = listItem.childNodes[0].textContent;
    const inputField = document.createElement('input');
    inputField.type = 'text';
    inputField.value = currentText;
    listItem.innerHTML = '';
    listItem.appendChild(inputField);
    listItem.appendChild(saveButton);
}