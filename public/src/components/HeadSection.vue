<template>
    <div class="wrapper">
        <div>
            <h1>Все товары</h1>
            <h2>Лучшие товары для вас</h2>
        </div>
        <div>
            <img src="/img/main-image.svg" alt="">
        </div>
    </div>
</template>

<script>
export default {}
</script>

<style scoped>
.wrapper {
    background: #5CDDBC;
    width: 104%;
    position: relative;
    right: 13%;
    display: flex;
    padding: 0 12%;
    justify-content: space-between;
    align-items: center;
    height: 240px;
    color: #216F5B;
    margin: 60px 0;
}

.wrapper h1 {
    font-size: 40px;
    font-weight: 800;
    margin-top: -15px;
}

.wrapper h2 {
    font-size: 24px;
    font-weight: 400;
    /* margin-top: px; */
}

.wrapper img {
    height: 230px;
    position: relative;
    top: 8px;
    right: 30px;
}
</style>