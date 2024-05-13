$(document).ready(function() { 
    $(document).on("click", '.delete-btn', function() {
        const noteId = $(this).val()

        $.ajax({
            type: 'POST',
            url: `delete-note/`,
            data: {
                note_id: noteId,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },

            success: (data) => {
                $(this).parent().parent().parent().parent().parent().hide()
                $("#delete-note-modal").delay(100).fadeIn().delay(50).fadeOut();
                console.log(data)
            }
        })
    });

    $(document).on('click', '#complete_note', function () {
        console.log($(this).attr('data-note-id'))
        const noteId = $(this).attr('data-note-id')

        $.ajax({
            type: 'POST',
            url: 'complete-note/',
            data: {
                note_id: noteId,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },

            success: (data) => {
                $(this).removeClass('btn-success').addClass('btn-warning').html('Активировать')
                $(this).attr('id', 'activate_note').attr('name', 'activate_note')
                // Убрать этот позор
                $(this).parent().parent().parent().parent().parent().removeClass('alert-warning').addClass('alert-info')
                console.log(data)
            }
        })
    })

    $(document).on('click', '#activate_note', function() {
        const noteId = $(this).val()

        $.ajax({
            type: 'POST',
            url: 'activate_note/',
            data: {
                note_id: noteId,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },

            success: (data) => {
                $(this).removeClass('btn-warning').addClass('btn-success').html('Выполненно')
                $(this).attr('id', 'complete_note').attr('name', 'complete_note')
                // Убрать этот позор
                $(this).parent().parent().parent().parent().parent().removeClass('alert-info').addClass('alert-warning')
                console.log(data)
            }
        })
    })

    $('#create-note-form').on('submit', function (e) {
        e.preventDefault()
        const noteName = $('#note_name').val()

        if (noteName.length < 1) {
            return
        }

        $.ajax({
            type: 'POST',
            url: 'create-note/',
            data: {
                name: noteName,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },

            success: (data) => {
                $('#create-note-modal').delay(100).fadeIn().delay(50).fadeOut()
                $("#note-list").append(
                    `
                    
              <div id="note-list" style="border-radius: 20px;" class="alert alert-warning">
                    <ul id="note-list" class="list-group list-group-horizontal rounded-0 bg-transparent">
                  <li
                    class="list-group-item px-3 py-1 d-flex align-items-center flex-grow-1 border-0 bg-transparent">
                    <span style="font-size: 24px;" class="lead fw-normal mb-0">${data.name} <span style="margin-left: 10px; font-size: 12px; font-weight: 500; color: grey;">Статус: <span id="{{ note.id }}-note-status" style="color: green;">активен</span></span></span>
                  </li>
                  <li class="list-group-item ps-3 pe-0 py-1 rounded-0 border-0 bg-transparent">
                    <div class="d-flex flex-row justify-content-end mb-1">
                      <a href="#!" class="text-info" data-mdb-tooltip-init title="Edit todo"><i
                          class="fas fa-pencil-alt me-3"></i></a>
                      <a href="#!" class="text-danger" data-mdb-tooltip-init title="Delete todo"><i
                          class="fas fa-trash-alt"></i></a>
                    </div>
                    <div class="text-end text-muted">
                      <form action="">
                        <button id="complete_note" data-note-id="${data.id}" name="complete_note" value="${data.id}" type="button" class="btn btn-success">Выполненно</button>
                        <button id="delete_note" name="delete_note" type="button" value="${data.id}" class="btn btn-danger delete-btn">Удалить</button>
                      </form>
                      <a href="#!" class="text-muted" data-mdb-tooltip-init title="Created date">
                        <p class="small mb-0"><i class="fas fa-info-circle me-2"></i>${data.date_created}</p>
                      </a>
                    </div>
                  </li>
                </ul>
                </div>
                    `
                )
                console.log(data)
            }
        })
    })
})
