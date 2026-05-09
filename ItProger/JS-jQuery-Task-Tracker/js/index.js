$(document).ready(function() {
    let tasksArray = [];

    $('#addBtn').on('click', function() {
        let taskText = $('#taskInput').val(); 

        if (taskText !== "") {
            tasksArray.push(taskText);
            $('#taskInput').val("");
            $('#notification').stop(true, true).fadeIn(200).delay(2000).fadeOut(200);
        }
    });

    $('#displayBtn').on('click', function() {
        let $taskList = $('#taskList');
        $taskList.empty();
        if (tasksArray.length > 0) {
            $.each(tasksArray, function(index, task) {
                let taskNumber = index + 1;
                $taskList.append('<div class="task-item"><i class="fa-regular fa-circle-check"></i> Завдання #' + taskNumber + ': ' + task + '</div>');
            });
        }
        
        $taskList.show();
    });
});