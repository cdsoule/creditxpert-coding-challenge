const gridContainer = document.getElementById('grid-container')

function renderGrid(currow, curcol, matrix) {
    gridContainer.innerHTML = ''
    matrix.forEach((row, i) => {
        row.forEach((cellValue, j) => {
            const cell = document.createElement('div');
            if (i == currow && j == curcol) {
                const ant = document.createElement('img')
                ant.src = '../static/ant.svg'
                ant.style.height = '30px'
                ant.className = 'ant'
                cell.appendChild(ant)
            }
            cell.className = 'cell d-flex';
            cell.style.backgroundColor = cellValue === 1 ? 'black' : 'white';
            gridContainer.appendChild(cell);
        })
    })
}

function visualizeMovement() {
    for (let i = 0; i < data.length; i++) {
        let currow = data[i].row
        let curcol = data[i].col
        let matrix = data[i].matrix
        setTimeout(() => {
            renderGrid(currow, curcol, matrix);
        }, i * 500);
    }
}

$('document').ready(visualizeMovement)