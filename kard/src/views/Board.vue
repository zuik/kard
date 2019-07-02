<template>
  <div class="container">
    <h1>Kard</h1>
    <b-row>
      <b-col>
        <Cards />
      </b-col>
    </b-row>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Cards from '@/components/Cards.vue'; // @ is an alias to /src

@Component({
  components: {
    Cards,
  },
})
export default class Board extends Vue {}
</script>
