/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author GenaThink
 */
public class Animales {
    public static void main(String[] args) {
        Perro perro = new Perro("Perro", "Pollito", "Mini Toy ");
        Gato gato = new Gato("Esfinje", "Wiskas", "Mediano");
        Pez pez = new Pez("Pez Payaso", "CangreBurguers", "Pequenio");
        Leon leon = new Leon("Sabana");
        
        perro.imprime();
        perro.hacerRuido();
        
        gato.comer("Come Mucho ");
        gato.imprime();
        gato.hacerRuido();
        
        pez.imprime();
        pez.hacerRuido();
        pez.getVacuna();
        leon.rugir();
    }
}
