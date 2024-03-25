let scheme

async function setColorScheme() {
    const schemeId = $('#color-select')[0].value
    scheme = await getColorSchemeById(schemeId)
    const colors = $(".colors")
    for (let i = 0; i < colors.length; i++) {
        colorIndex = [...colors[i].classList].pop()
        colors[i].style.color = scheme[colorIndex]
    }
}

async function setShape() {
    const shapeId = $('#shape-select')[0].value
    const shape = await getShapeById(shapeId)
    const shapes = $(".shapes")
    for (let i = 0; i < shapes.length; i++) {
        shapes[i].className = `shapes ${shape.fa_class}`
    }
}

function makeDraggable(element) {
    let offsetX, offsetY;
    const zoneOne = document.getElementById('zone-one');
    const zoneTwo = document.getElementById('zone-two');
    const zoneThree = document.getElementById('zone-three');

    function handleMouseDown(e) {
        offsetX = e.clientX - element.getBoundingClientRect().left;
        offsetY = e.clientY - element.getBoundingClientRect().top;

        document.addEventListener('mousemove', handleMouseMove);
        document.addEventListener('mouseup', handleMouseUp);
    }

    function handleMouseMove(e) {
        element.style.left = e.clientX - offsetX + 'px';
        element.style.top = e.clientY - offsetY + 'px';
        element.style.transform = ''
        setShapeColor(element)
    }

    function handleMouseUp() {
        document.removeEventListener('mousemove', handleMouseMove);
        document.removeEventListener('mouseup', handleMouseUp);
    }

    function setShapeColor(element) {
        const shapeRect = element.getBoundingClientRect();
        const zoneOneRect = zoneOne.getBoundingClientRect();
        const zoneTwoRect = zoneTwo.getBoundingClientRect();
        const zoneThreeRect = zoneThree.getBoundingClientRect();

        if (
            shapeRect.left >= zoneOneRect.left &&
            shapeRect.right <= zoneOneRect.right &&
            shapeRect.top >= zoneOneRect.top &&
            shapeRect.bottom <= zoneOneRect.bottom
        ) {
            element.style.color = scheme.color1;
        } else if (
            shapeRect.left >= zoneTwoRect.left &&
            shapeRect.right <= zoneTwoRect.right &&
            shapeRect.top >= zoneTwoRect.top &&
            shapeRect.bottom <= zoneTwoRect.bottom
        ) {
            element.style.color = scheme.color2;
        } else if (
            shapeRect.left >= zoneThreeRect.left &&
            shapeRect.right <= zoneThreeRect.right &&
            shapeRect.top >= zoneThreeRect.top &&
            shapeRect.bottom <= zoneThreeRect.bottom
        ) {
            element.style.color = scheme.color3;
        } else {
            element.style.color = scheme.color4;
        }
    }

    element.addEventListener('mousedown', handleMouseDown);
}

$('document').ready(() => {
    const shapeElement = document.getElementById("shape")
    makeDraggable(shapeElement)}
)