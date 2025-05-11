<script>
  import Header from '../components/Header.vue';
  import HeadSection from '@/components/HeadSection.vue';
  import ItemsSection from '@/components/ItemsSection.vue';
  import Form_Edit from '@/components/Form_Edit.vue';

  
  export default {
    props:['basket', 'addToBasket'],
    components: {Header, HeadSection, ItemsSection, Form_Edit}
  }  
</script>

<template>
  <div>

    <Header :basket="basket" />
    <HeadSection  />
    <ItemsSection :addToBasket="addToBasket" />
  </div>
  
</template>