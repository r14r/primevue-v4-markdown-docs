<Galleria :value="images" :responsiveOptions="responsiveOptions" :numVisible="5" :circular="true" containerStyle="max-width: 640px">
    <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block" />
    </template>
    <template #thumbnail="slotProps">
        <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block" />
    </template>
</Galleria>