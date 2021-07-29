/*

Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

MaiorAB = (a + b + abs(a-b))
          ------------------
                  2

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

*/



//Import necessário para trabalhar com leitura dirato pelo console
const readLine = require('readline');

// Cria uma constante que possui a interface para pegar o stdin e stdout
const rl = readLine.createInterface({
    input : process.stdin,
    output : process.stdout
});

//Função que recebe os três números e retorna o maior deles
function ehMaior(a, b, c) {
    
    let ab = (a + b + (Math.abs(a - b))) / 2;    
    let maior = ab > c ? ab  : c;

    return   `${maior} eh o maior`;

}

// Habilita o console para receber as entradas.
rl.on('line', (entrada) => {

    let [a, b, c] = entrada.split(' ').map(n => parseFloat(n));

    console.log(ehMaior(a, b, c));
    
    rl.close();
});

