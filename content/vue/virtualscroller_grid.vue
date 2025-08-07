<VirtualScroller :items="items" :itemSize="[50, 100]" orientation="both" class="border border-surface-200 dark:border-surface-700 rounded" style="width: 200px; height: 200px">
    <template v-slot:item="{ item, options }">
        <div :class="['flex items-center p-2', { 'bg-surface-100 dark:bg-surface-700': options.odd }]" style="height: 50px">
            <template v-for="(el, index) of item" :key="index">
                <div style="width: 100px">{{ el }}</div>
            </template>
        </div>
    </template>
</VirtualScroller>