window.onload = function () {
  const notes = document.querySelectorAll(".open_notes_modal");
  notes.forEach((el) => {
    el.addEventListener("click", function (e) {
      note_id = e.target.closest(".open_notes_modal").dataset.noteId;
      const myModal = new bootstrap.Modal(
        document.getElementById("showNoteModal"),
        {}
      );
      myModal.show();
      document
        .getElementById("showNoteModal")
        .addEventListener("shown.bs.modal", function (event) {
          event.target.querySelector(".modal-title.note-title").innerText =
            null;
          event.target.querySelector(".modal-body.note-content").innerText =
            null;
          fetch(`http://localhost:8000/notes/${note_id}/`, {
            headers: {
              accept:
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
              "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
              "cache-control": "max-age=0",
              "sec-ch-ua":
                '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
              "sec-ch-ua-mobile": "?0",
              "sec-ch-ua-platform": '"macOS"',
              "sec-fetch-dest": "document",
              "sec-fetch-mode": "navigate",
              "sec-fetch-site": "none",
              "sec-fetch-user": "?1",
              "upgrade-insecure-requests": "1",
            },
            referrerPolicy: "strict-origin-when-cross-origin",
            body: null,
            method: "GET",
            mode: "cors",
            credentials: "include",
          })
            .then((response) => {
              if (response.ok) {
                return response.json();
              }
              throw new Error("Something went wrong");
            })
            .then((data) => {
              console.log(data);
              console.log(event.target);
              event.target.querySelector(".modal-title.note-title").innerText =
                data.title;
              event.target.querySelector(".modal-body.note-content").innerText =
                data.content;
            });
        });
    });
  });
};
