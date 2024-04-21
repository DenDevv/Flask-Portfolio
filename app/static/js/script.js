const icons = document.querySelectorAll('.icons img');

document.addEventListener('mousemove', (event) => {
    const mouseX = event.clientX;
    const mouseY = event.clientY;

    const figures = [
        ["figure1", 1],
        ["figure2", 3],
        ["figure3", 2],
        ["figure4", 4],
        ["figure5", 1],
        ["figure6", 2],
        ["figure7", 4],
        ["figure8", 2],
        ["figure9", 3],
        ["figure10", 1],
        ["figure11", 4],
        ["figure12", 3],
        ["figure13", 2],
        ["figure14", 1]
    ];

    function moveIcon(figure_id, side) {
        let icon = document.getElementById(figure_id);
        const iconX = icon.getBoundingClientRect().left + icon.offsetWidth / 2;
        const iconY = icon.getBoundingClientRect().top + icon.offsetHeight / 2;

        let distanceX, distanceY;

        switch (side) {
            case 1: 
                distanceX = mouseX - iconX;
                distanceY = mouseY - iconY;
                break;
            
            case 2:
                distanceX = iconX - mouseX;
                distanceY = mouseY - iconY;
                break;

            case 3:
                distanceX = mouseX - iconX;
                distanceY = iconY - mouseY;
                break;

            default:
                distanceX = iconX - mouseX;
                distanceY = iconY - mouseY;
                break;
        }

        const translateX = distanceX * 0.1;
        const translateY = distanceY * 0.1;

        icon.style.transform = `translateX(${translateX}px) translateY(${translateY}px)`;
    };

    for (let i = 0; i < figures.length; i++) {
        moveIcon(figures[i][0], figures[i][1]);
    };

});
