<template>
    <v-dialog v-model="dialog" persistent max-width="600px">
        <v-btn slot="activator" flat>
            Editar Examen
        </v-btn>
        <v-card>
            <v-card-title>
            <span class="headline">Editar Examen</span>
            </v-card-title>
<p>Editar nombre del examen</p>
        <v-flex xs12 sm6>
            <v-text-field
                v-model="name"
                :label="filteredExam.name"
            ></v-text-field>
        </v-flex>
<p>Editar encabezado del examen</p>
        <v-flex xs12 sm6>
            <v-text-field
                v-model="encabezado"
                :label="filteredExam.encabezado"
            ></v-text-field>
        </v-flex>
        <p>Cantidad de preguntas</p>
        <v-flex xs12 sm4>
        <v-overflow-btn
          :items="cantidad"
          target="#dropdown-example"
          item-value="text"
          v-model="cantidad"
        ></v-overflow-btn>
        </v-flex >

        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="green darken-1" flat @click.native="dialog = false">Cancelar</v-btn>
            <v-btn color="green darken-1" flat v-on:click="editExam(name, encabezado, cantidad)" >Guardar</v-btn>
        </v-card-actions>

        </v-card>
    </v-dialog>
</template>
<script>
import CrearVariable from './CrearVariable.vue'
export default {
  data () {
    return {
      dialog: false,
      tema: undefined,
      tipoPregunta: undefined, // Guarda que tipo de pregunta es
      respuestaVoF: undefined, // Guarda si la pregunta tiene valor de V o F
      pregunta: undefined, // Guardo la pregunta
      respuestaOM: undefined,
      dummyAnswers: [],
      dummyAnswer: undefined,
      variables: [],
      cantidad: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    }
  },
  components: {
    'CrearVariable': CrearVariable
  },
  props: {
    exam: {
      required: true
    },
    selectedExam: {
      required: true
    }
  },
  methods: {
    editExam (nombre, encabezado, cantidad) {
      let payload = [nombre, encabezado, this.selectedExam, cantidad]
      // console.log(payload)
      this.$store.dispatch('editExam', payload)
        .then((response) => {
          this.dialog = false
        })
        .catch((error) => {
          console.log('Error')
          console.log(error)
        })
    }
  },
  computed: {
    filteredExam () {
      var EExam = this.exam
      EExam = EExam.filter((YaBasta) => {
        return YaBasta.test_id === this.selectedExam
      })
      return EExam[0]
    }
  }
}
</script>
