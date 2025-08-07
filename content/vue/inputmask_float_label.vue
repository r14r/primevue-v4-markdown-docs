<FloatLabel>
    <InputMask id="over_label" v-model="value1" mask="999-99-9999" />
    <label for="over_label">Over Label</label>
</FloatLabel>

<FloatLabel variant="in">
    <InputMask id="in_label" v-model="value2" mask="999-99-9999" variant="filled" />
    <label for="in_label">In Label</label>
</FloatLabel>

<FloatLabel variant="on">
    <InputMask id="on_label" v-model="value3" mask="999-99-9999" />
    <label for="on_label">On Label</label>
</FloatLabel>