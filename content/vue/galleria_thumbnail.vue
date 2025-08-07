<Galleria :value="images" :responsiveOptions="responsiveOptions" :numVisible="5" :thumbnailsPosition="position" containerStyle="max-width: 640px">
    <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block" />
    </template>
    <template #thumbnail="slotProps">
        <div class="grid gap-4 justify-center">
            <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="width: 100%; display: block;" />
        </div>
    </template>
</Galleria>