/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author GenaThink
 */
public class Pez extends Mascota{
    public String vacuna;

    public Pez() {
    }

    public Pez(String foto, String comida, String tamanio) {
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
       System.out.println("GLU GLU GLU GLU");
    }
}
