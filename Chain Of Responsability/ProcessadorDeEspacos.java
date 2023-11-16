public class ProcessadorDeEspacos implements Processador {
    private Processador sucessor = new ProcessadorDeLetras_A_e_C();

    public Object processarRequisicao(String requisicao) {
        int cont = requisicao.length() - requisicao.replaceAll(" ","").length();
        System.out.println("\" \" -> " + cont);
        return sucessor.processarRequisicao(requisicao);
    }
}
