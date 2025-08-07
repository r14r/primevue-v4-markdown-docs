<div class="flex flex-wrap justify-center gap-2 mb-2">
    <Button label="Left" icon="pi pi-arrow-right" @click="openPosition('left')" severity="secondary" style="min-width: 10rem" />
    <Button label="Right" icon="pi pi-arrow-left" @click="openPosition('right')" severity="secondary" style="min-width: 10rem" />
</div>
<div class="flex flex-wrap justify-center gap-2 mb-2">
    <Button label="TopLeft" icon="pi pi-arrow-down-right" @click="openPosition('topleft')" severity="secondary" style="min-width: 10rem" />
    <Button label="Top" icon="pi pi-arrow-down" @click="openPosition('top')" severity="secondary" style="min-width: 10rem" />
    <Button label="TopRight" icon="pi pi-arrow-down-left" @click="openPosition('topright')" severity="secondary" style="min-width: 10rem" />
</div>
<div class="flex flex-wrap justify-center gap-2">
    <Button label="BottomLeft" icon="pi pi-arrow-up-right" @click="openPosition('bottomleft')" severity="secondary" style="min-width: 10rem" />
    <Button label="Bottom" icon="pi pi-arrow-up" @click="openPosition('bottom')" severity="secondary" style="min-width: 10rem" />
    <Button label="BottomRight" icon="pi pi-arrow-up-left" @click="openPosition('bottomright')" severity="secondary" style="min-width: 10rem" />
</div>

<Dialog v-model:visible="visible" header="Edit Profile" :style="{ width: '25rem' }" :position="position" :modal="true" :draggable="false">
    <span class="text-surface-500 dark:text-surface-400 block mb-8">Update your information.</span>
    <div class="flex items-center gap-4 mb-4">
        <label for="username" class="font-semibold w-24">Username</label>
        <InputText id="username" class="flex-auto" autocomplete="off" />
    </div>
    <div class="flex items-center gap-4 mb-8">
        <label for="email" class="font-semibold w-24">Email</label>
        <InputText id="email" class="flex-auto" autocomplete="off" />
    </div>
    <div class="flex justify-end gap-2">
        <Button type="button" label="Cancel" severity="secondary" @click="visible = false"></Button>
        <Button type="button" label="Save" @click="visible = false"></Button>
    </div>
</Dialog>