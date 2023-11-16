public class ProcessadorDePontos implements Processador {
    public Object processarRequisicao(String requisicao) {
        long cont = requisicao.chars().filter(c -> c == '.').count();
        System.out.println("\".\" -> " + cont);
        return requisicao;
    }
}
