class Turma {
    constructor(numero, prof, turno, pareceres) {
        this.numero = numero;
        this.turno = turno;
        this.pareceres = pareceres;
        this.prof = prof
    }
    get() {
        return this
    }
    set(turma) {
        this = turma
    }
}