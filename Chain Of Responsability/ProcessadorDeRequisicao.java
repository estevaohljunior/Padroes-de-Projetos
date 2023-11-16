public class ProcessadorDeRequisicao implements Processador{
    private Processador sucessor = new ProcessadorDeEspacos();
    public Object processarRequisicao(String requisicao) {
        requisicao = requisicao.toLowerCase();
        System.out.println("Número de cacteres:");
        return sucessor.processarRequisicao(requisicao);
    }
}
