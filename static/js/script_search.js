//eu sinceramente, so copiei e colei a função parseCSV, pq vsfd
function parseCSV(csvText) {
    const linhas = csvText.split('\n').filter(linha => linha.trim() !== '');
    const resultado = [];
    
    if (linhas.length === 0) return resultado;
    
    const cabecalho = linhas[0].split(',').map(item => item.trim());
    
    for (let i = 1; i < linhas.length; i++) {
        const obj = {};
        const valores = linhas[i].split(',');
        
        cabecalho.forEach((coluna, index) => {
            obj[coluna] = valores[index] ? valores[index].trim() : '';
        });
        
        resultado.push(obj);
    }
    
    return resultado;
}

fetch('/data.csv')
    .then(res => res.text())
    .then((csvText) => {
        
        const plant = parseCSV(csvText);
        const ul = document.querySelector('#sugestionList');
        plant.forEach((item) => {
            const li = document.createElement("li");
            li.innerHTML = `
                <button onclick="submitSugestion('${item['Nome Popular']}')" type="button" class="buttonList">
                    <span class="plantName">${item['Nome Popular']}</span>
                </button>
            `;
            ul.appendChild(li);
        });
    })


function submitSugestion(plantName)
{
    if (!plantName) return;
    window.location.href = `/plantas/${encodeURIComponent(plantName)}`;
}

function searchPlant()
{
    const input = document.querySelector('#search-input');
    if (!input || !input.value.trim()) return;
    
    const plantName = input.value.trim();
    window.location.href = `/plantas/${encodeURIComponent(plantName)}`;
}

function filter()
{
    var input,
        filter,
        ul,
        i,
        span,
        txtValue,
        li,
        count = 0;

        input = document.querySelector('#search-input');
        ul = document.querySelector('#sugestionList');
        
        //filtro
        filter = input.value.toUpperCase();

        //todas as li da lista
        li = ul.getElementsByTagName("li");

        if (filter == "")
        {
            ul.style.display = "none"
            return;
        }

        for (i = 0; i < li.length; i++)
        {
            //pegar o span com o nome da planta
            span = li[i].querySelector(".plantName");
            //texto dentro da tag button
            txtValue = span.textContent.trim();
            //verificar se a letra é igual
            if(txtValue.toUpperCase().indexOf(filter) > -1)
            {
                //valor bateu
                li[i].style.display = "";
                count++;

                if (span)
                {
                    span.innerHTML = txtValue.replace(new RegExp(filter, "gi"), (match) => {
                    return "<strong>" + match + "</strong>"
                    })
                }
                if (count > 5)
                {
                    li[i].style.display = "none";
                }
                else
                {
                    li[i].style.display = "block";
                }
            }
            else
            {
                li[i].style.display = "none";
            }
        }

        if (count === 0)
        {
            ul.style.display = "none";
        }
        else 
        {
            ul.style.display = "block";
        }
}
const button = document.querySelector('#buttonLOGO');

button.addEventListener('click', () => {
    open('/', '_self');
})
button.addEventListener('contextmenu', (e) => {
    e.preventDefault();
})