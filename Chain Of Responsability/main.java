public class Main {
    public static void main(String[] args) throws Exception {
        new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
        String requisicao = new String("Luiz aacca. Medeiros .ccaca Neto. aa.cc..");
        Processador p = new ProcessadorDeRequisicao();
        p.processarRequisicao(requisicao);
        requisicao = null;
    }
}
