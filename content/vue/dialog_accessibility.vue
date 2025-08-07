<Button label="Show" icon="pi pi-external-link" @click="visible = true" :aria-controls="visible ? 'dlg' : null" :aria-expanded="visible ? true : false" />

<Dialog id="dlg" header="Header" v-model:visible="visible" :style="{ width: '50vw' }">
    <p>Content</p>
</Dialog>