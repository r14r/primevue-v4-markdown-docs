<div>
    <Button icon="pi pi-minus" @click="prev" />
    <Button icon="pi pi-plus" @click="next" severity="secondary" class="ml-2" />
</div>

<Galleria v-model:activeIndex="activeIndex" :value="images" :responsiveOptions="responsiveOptions" :numVisible="5" containerStyle="max-width: 640px">
    <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%" />
    </template>
    <template #thumbnail="slotProps">
        <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" />
    </template>
</Galleria>