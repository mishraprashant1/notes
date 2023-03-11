window.onload = function () {
  const notes = document.querySelectorAll(".open_notes_modal");

  const fetch_note = async function (note_id) {
    const response = await fetch(`http://localhost:8000/notes/${note_id}/`);
    const data = await response.json();
    return data;
  };

  const handleRowClick = async function (e) {
    if (
      e.target.classList.contains("edit-note-button") |
      (e.target.closest(".edit-note-button") != null)
    )
      return;
    const note_id = e.target.closest(".open_notes_modal").dataset.noteId;
    const notes_modal = new bootstrap.Modal(
      document.getElementById("showNoteModal"),
      {}
    );

    const notes_modal_el = document.getElementById("showNoteModal");
    notes_modal_el.querySelector(".modal-title.note-title").innerHTML = `
        <div class="spinner-border text-info" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
    `;
    notes_modal_el.querySelector(".modal-body.note-content").innerHTML = `
        <div class="spinner-border text-info" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
    `;

    notes_modal.show();

    const data = await fetch_note(note_id);

    notes_modal_el.querySelector(".modal-title.note-title").innerText =
      data.title;
    notes_modal_el.querySelector(".modal-body.note-content").innerText =
      data.content;
  };

  notes.forEach((el) => {
    el.addEventListener("click", handleRowClick);
  });
};
