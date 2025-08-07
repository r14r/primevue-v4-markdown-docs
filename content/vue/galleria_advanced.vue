<Galleria
    ref="galleria"
    v-model:activeIndex="activeIndex"
    :value="images"
    :numVisible="5"
    containerStyle="max-width: 640px"
    :showThumbnails="showThumbnails"
    :showItemNavigators="true"
    :showItemNavigatorsOnHover="true"
    :circular="true"
    :autoPlay="isAutoPlay"
    :transitionInterval="3000"
    :responsiveOptions="responsiveOptions"
    :pt="{
        root: {
            class: [{ 'flex flex-col': fullScreen }]
        },
        content: {
            class: ['relative', { 'flex-1 justify-center': fullScreen }]
        },
        thumbnails: 'absolute w-full left-0 bottom-0'
    }"
>
    <template #item="slotProps">
        <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" :style="[{ width: !fullScreen ? '100%' : '', display: !fullScreen ? 'block' : '' }]" />
    </template>
    <template #thumbnail="slotProps">
        <div class="grid gap-4 justify-center">
            <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="display: block" />
        </div>
    </template>
    <template #footer>
        <div class="flex items-stretch bg-surface-950 text-white h-10">
            <button type="button" @click="onThumbnailButtonClick" class="bg-transparent border-none rounded-none hover:bg-white/10 text-white inline-flex justify-center items-center cursor-pointer px-3">
                <i class="pi pi-th-large"></i>
            </button>
            <button type="button" @click="toggleAutoSlide" class="bg-transparent border-none rounded-none hover:bg-white/10 text-white inline-flex justify-center items-center cursor-pointer px-3"><i :class="slideButtonIcon"></i></button>
            <span v-if="images" class="flex items-center gap-4 ml-3">
                <span class="text-sm">{{ activeIndex + 1 }}/{{ images.length }}</span>
                <span class="font-bold text-sm">{{ images[activeIndex].title }}</span>
                <span class="text-sm">{{ images[activeIndex].alt }}</span>
            </span>
            <button type="button" @click="toggleFullScreen" class="bg-transparent border-none rounded-none hover:bg-white/10 text-white inline-flex justify-center items-center cursor-pointer px-3 ml-auto">
                <i :class="fullScreenIcon"></i>
            </button>
        </div>
    </template>
</Galleria>