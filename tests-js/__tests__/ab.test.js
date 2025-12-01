const {
  VARIANDID,
  valiVariant,
  vahetaVariant,
  looLayoutHTML,
  looSyndmuseKeha,
} = require("../../frontend/ab.js");

describe("A/B loogika", () => {
  test("valiVariant tagastab olemasoleva variandi", () => {
    const tulemus = valiVariant("variant_b", { sessioonId: "sess-1" });
    expect(tulemus.variant).toBe("variant_b");
    expect(tulemus.sessioonId).toBe("sess-1");
  });

  test("valiVariant kasutab juhuarvu deterministlikult", () => {
    const tulemus = valiVariant(null, { juhuarv: () => 0.99 });
    expect(VARIANDID).toContain(tulemus.variant);
  });

  test("vahetaVariant annab teise variandi", () => {
    expect(vahetaVariant("variant_a")).toBe("variant_b");
    expect(vahetaVariant("variant_b")).toBe("variant_a");
  });

  test("looLayoutHTML sisaldab variandi märksõnu", () => {
    expect(looLayoutHTML("variant_a")).toContain("Variant A");
    expect(looLayoutHTML("variant_b")).toContain("Variant B");
  });

  test("looSyndmuseKeha lisab metaandmed", () => {
    const keha = looSyndmuseKeha("variant_a", "katse", { sessioonId: "sess" });
    expect(keha.variant).toBe("variant_a");
    expect(keha.katsestaadium).toBe("katse");
    expect(keha.sessioonId).toBe("sess");
  });
});

// salvestamine
describe("salvestamine", () => {
  // beforeEach: loome enne iga testi lihtsa mock localStorage meetoditega setItem, getItem ja clear
  beforeEach(() => {
    // lihtne mock localStorage jaoks
    global.localStorage = {
      store: {},
      // setItem salvestab väärtuse võtme järgi salvestusse
      setItem(key, value) { 
        this.store[key] = value; 
      },
      // getItem tagastab väärtuse võtme järgi store'ist
      getItem(key) { 
        return this.store[key]; 
      },
      // clear puhastab store
      clear() { 
        this.store = {}; 
      }
    };
  });
  // kontrollib, et andmed salvestatakse korrektselt localStorage'isse
  test("andmete salvestamine localStorage-sse", () => {
    const data = { variant: "variant_a", sessioonId: "sess-123" };
    // Salvestame objekti localStorage'is võtme ‚ab_data‘ all
    localStorage.setItem("ab_data", JSON.stringify(data));
    // Saame salvestatud andmed ja parsimine tagasi objektisse
    const salvestatud = JSON.parse(localStorage.getItem("ab_data"));
    // Kontrollime, et andmed on korrektselt salvestatud
    expect(salvestatud.variant).toBe("variant_a");
    expect(salvestatud.sessioonId).toBe("sess-123");
  });
});
