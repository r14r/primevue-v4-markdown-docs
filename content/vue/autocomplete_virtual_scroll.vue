<AutoComplete v-model="selectedItem" :suggestions="filteredItems" @complete="searchItems"
    :virtualScrollerOptions="{ itemSize: 38 }" optionLabel="label" dropdown />