<Galleria :value="images" :responsiveOptions="responsiveOptions" :numVisible="5" containerStyle="max-width: 640px"
    :circular="true" :autoPlay="true" :transitionInterval="2000">
    <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block" />
    </template>
    <template #thumbnail="slotProps">
        <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="display: block" />
    </template>
</Galleria>