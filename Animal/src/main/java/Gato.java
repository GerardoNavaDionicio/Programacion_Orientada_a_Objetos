/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author GenaThink
 */
public class Gato extends Mascota{
     public String vacuna;

    public Gato() {
    }

    public Gato(String foto, String comida, String tamanio) {
        super(foto, comida, tamanio);
    }

    public String getVacuna() {
        return vacuna;
    }

    public void setVacuna(String vacuna) {
        this.vacuna = vacuna;
    }
    
    public void imprime(){
        System.out.println("\n" + getFoto() +"\n"+ getComida() + "\n"+ getTamanio());
    }
    @Override
    public void hacerRuido() {
        System.out.println("Hace el siguiente ruido: Mew Mew");; //To change body of generated methods, choose Tools | Templates.
    }
    
}
