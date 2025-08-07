<div class="flex flex-wrap gap-2 mb-6">
    <Button type="button" icon="pi pi-plus" label="Expand All" @click="expandAll" />
    <Button type="button" icon="pi pi-minus" label="Collapse All" @click="collapseAll" />
</div>
<Tree v-model:expandedKeys="expandedKeys" :value="nodes" class="w-full md:w-[30rem]"></Tree>