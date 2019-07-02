<template>
  <b-card class="kard">
    <b-card-body class="kard-body">
      <div class="kard-text">
        Question going to be here:
        <h1>Blah blah</h1>
      </div>
      <div class="kard-answer">
        <div class="input-group input-group-lg">
          <div class="input-group-prepend">
            <span class="input-group-text" id="inputGroup-sizing-lg"
              >Answer</span
            >
          </div>
          <input
            type="text"
            class="form-control"
            aria-label="Sizing example input"
            aria-describedby="inputGroup-sizing-lg"
          />
        </div>
      </div>
    </b-card-body>
  </b-card>
</template>

<style lang="scss">
.kard {
  width: 40em;
  height: 20em;
  margin: 1em auto;
  text-align: center;
  .kard-body {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 100%;
    height: 100%;
  }
}
</style>
