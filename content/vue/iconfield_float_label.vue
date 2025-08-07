<FloatLabel>
    <IconField>
        <InputIcon class="pi pi-search" />
        <InputText id="over_label" v-model="value1" autocomplete="off" />
    </IconField>
    <label for="over_label">Over Label</label>
</FloatLabel>

<FloatLabel variant="in">
    <IconField>
        <InputIcon class="pi pi-search" />
        <InputText id="in_label" v-model="value2" autocomplete="off" variant="filled" />
    </IconField>
    <label for="in_label">In Label</label>
</FloatLabel>

<FloatLabel variant="on">
    <IconField>
        <InputIcon class="pi pi-search" />
        <InputText id="on_label" v-model="value3" autocomplete="off" />
    </IconField>
    <label for="on_label">On Label</label>
</FloatLabel>