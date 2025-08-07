<Button label="Show" icon="pi pi-external-link" @click="visible = true" :aria-controls="visible ? 'sbar' : null" :aria-expanded="visible"/>

<Drawer id="sbar" v-model:visible="visible" role="region" >
    <p>Content</p>
</Drawer>