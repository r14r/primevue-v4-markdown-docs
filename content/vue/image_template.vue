<Image alt="Image" preview>
    <template #previewicon>
        <i class="pi pi-search"></i>
    </template>
    <template #image>
        <img src="/thumbnail.jpg" alt="image" />
    </template>
    <template #preview="slotProps">
        <img src="/image.jpg" alt="preview" :style="slotProps.style" @click="slotProps.onClick" />
    </template>
</Image>