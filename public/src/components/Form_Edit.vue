<template>
    <div>
        <button @click="edit = !edit">Редактировать</button>

        <form v-if="edit">
            <input placeholder="Фото" v-model="image" />
            <input placeholder="Введите название" v-model="title" />
            <input placeholder="Анонс" v-model="desc" />
            <input placeholder="Цена" v-model="price" />
            <button type="button" @click="editData()">Обновить</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    props: ['item'],
    data() {
        return {
            edit: false,
            
            image: this.item.image,
            title: this.item.title,
            desc: this.item.desc,
            price: this.item.price,
        }
    },
    methods: {

        async editData() {
            try {

                const data = {
                    'image': this.image,
                    'title': this.title,
                    'desc': this.desc,
                    'price': this.price
                }
                
                const res = await axios.put(`http://127.0.0.1:8000/api/edit-item/${this.item.slug}`, data)
                if(res.data.result === "Done")
                    this.edit = false
            } catch(error) {
                console.log(error)
            }
        }
    }
}
</script>

<style scoped>

</style>