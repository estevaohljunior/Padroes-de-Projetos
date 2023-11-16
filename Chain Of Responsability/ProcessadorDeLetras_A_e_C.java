public class ProcessadorDeLetras_A_e_C implements Processador {
    private Processador sucessor = new ProcessadorDePontos();

    public Object processarRequisicao(String requisicao) {

        int cont = requisicao.length() - requisicao.replaceAll("a", "").length();
        System.out.println("\"a\" -> " + cont);
        
        cont = requisicao.length() - requisicao.replaceAll("c", "").length();
        System.out.println("\"c\" -> " + cont);
        
        return sucessor.processarRequisicao(requisicao);
    }
}
