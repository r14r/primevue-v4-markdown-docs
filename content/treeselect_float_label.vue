<FloatLabel class="w-full md:w-80">
    <TreeSelect v-model="value1" inputId="over_label" :options="nodes" class="w-full" />
    <label for="over_label">Over Label</label>
</FloatLabel>

<FloatLabel class="w-full md:w-80" variant="in">
    <TreeSelect v-model="value2" inputId="in_label" :options="nodes" class="w-full" variant="filled" />
    <label for="in_label">In Label</label>
</FloatLabel>

<FloatLabel class="w-full md:w-80" variant="on">
    <TreeSelect v-model="value3" inputId="on_label" :options="nodes" class="w-full" />
    <label for="on_label">On Label</label>
</FloatLabel>