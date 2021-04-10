var valor; //define variável valor e resultado
var resultado; 
function botao(num){ //cria uma função botão que recebe num
    valor= document.calc.visor.value += num; // valor, em JavaScript recebe value do html
} //também concatena os valores apertados nos botões
function reseta(){ //cria uma função que reseta a calculadora
    document.calc.visor.value = '';//limpa o visor
}
function calcula(){ //cria uma função que calcula os valores
    resultado=eval(valor); //dá valor à uma string que tem uma operação matemática nela
    document.calc.visor.value=resultado.toLocaleString('pt-BR'); //formatado em pt-BR
}