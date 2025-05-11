<script>
  import Header from '../components/Header.vue';
  
  export default {
    props:['basket', 'addToBasket'],
    components: {Header}
  }  
</script>

<template>
  <div>
    <Header :basket="basket" />
    <h1>Доставка</h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quidem repellat placeat architecto nam facere nisi sapiente distinctio ea molestiae, natus voluptatibus, eveniet, officia tempora incidunt at. Asperiores, tempora! Delectus, nostrum.</p><br>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quidem repellat placeat architecto nam facere nisi sapiente distinctio ea molestiae, natus voluptatibus, eveniet, officia tempora incidunt at. Asperiores, tempora! Delectus, nostrum.</p><br>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quidem repellat placeat architecto nam facere nisi sapiente distinctio ea molestiae, natus voluptatibus, eveniet, officia tempora incidunt at. Asperiores, tempora! Delectus, nostrum.</p><br>
  </div>
  
</template>
<style>
h1 {
    margin-top: 150px;
    font-weight: 400;
    font-size: 90px;
}

p {
    font-size: 18px;
    margin: 20px 0;
}
</style>