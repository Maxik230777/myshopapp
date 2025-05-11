<script>
  import { RouterView } from "vue-router";

  export default {
    data() {
      return {
        basket:[]
      }
    },
    methods: {
      addToBasket(item) {
        let found = false
        this.basket.forEach( el => {
          if(el.slug == item.slug){
            found = true
            return
          }
                       
        })
        if (found) return
        // если не сработал ни один из return'ов то добавляем к массиву выбранный элемент
        this.basket.push(item);
      },
      // в этой функции будем фильтровать массив таким образом, чтобы slug элементов не был равен slug того элемента, который является аргументом  этого метода
      deleteFromBasket(slug) {
        this.basket = this.basket.filter(el =>{
          return el.slug !=slug
        });
        
        }
    }
  }
</script>

<template>
  <div class="container">
    <RouterView :basket="basket" :addToBasket="addToBasket" :deleteFromBasket ="deleteFromBasket" />
  </div>
</template>

<style scoped>

</style>
