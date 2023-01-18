function toggleFunc() {
    let input = document.getElementById('content');

    input.onkeydown = function (event) {

        if (event.which == 8 || event.which == 46) {

            event.preventDefault();   // turn off browser transition to the previous page 
        }
    };
}

