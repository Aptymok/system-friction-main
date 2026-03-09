<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>System Friction Lab | v.Beta</title>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;500&display=swap" rel="stylesheet">
    <style>
        :root {
            --accent: #0044ff; /* Azul Eléctrico */
            --accent-dim: rgba(0, 68, 255, 0.1);
            --bg: #ffffff;
            --text: #121212;
            --text-dim: #666;
            --r: 4px;
            --mono: 'JetBrains Mono', monospace;
            --nti-val: 45; /* Variable para Montecarlo */
        }

        body {
            background-color: var(--bg);
            color: var(--text);
            font-family: var(--mono);
            margin: 0;
            padding: 40px;
            line-height: 1.5;
            transition: background-color 0.8s ease;
        }

        /* Indicador de Estado Dinámico (Semáforo de fondo) */
        .status-low { background-color: #f4f7ff; } /* Verde/Azul suave */
        .status-mid { background-color: #fffdf0; } /* Amarillo alerta */
        .status-high { background-color: #fff5f5; } /* Rojo crisis */

        .doc-container { max-width: 900px; margin: 0 auto; position: relative; z-index: 10; }
        
        /* CABECERA DYNAMICS */
        .metrics-header {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin-bottom: 50px;
            border: 1px solid var(--accent);
            padding: 20px;
        }

        .scorecard { border-left: 3px solid var(--accent); padding-left: 15px; }
        .scorecard .val { font-size: 1.5rem; font-weight: 500; color: var(--accent); }
        .scorecard .label { font-size: 0.6rem; text-transform: uppercase; color: var(--text-dim); }

        /* ECG ANIMATION - EJE FIJO */
        .ecg-box {
            width: 100%;
            height: 100px;
            border-bottom: 1px solid var(--accent-dim);
            position: relative;
            margin: 40px 0;
            overflow: hidden;
        }
        .ecg-line {
            width: 200%;
            height: 2px;
            background: var(--accent);
            position: absolute;
            top: 50%;
            box-shadow: 0 0 10px var(--accent);
            animation: moveLine 4s infinite linear;
        }
        @keyframes moveLine {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }

        h1 { font-size: 2.2rem; font-weight: 300; line-height: 1.1; margin: 2rem 0; }
        .doc-label { font-size: 0.65rem; text-transform: uppercase; color: var(--accent); letter-spacing: 2px; }
        .rule { height: 1px; background: var(--accent-dim); margin: 2rem 0; }

        /* GRID DE DOCUMENTOS - ESTILO ORIGINAL */
        .doc-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; }
        .doc-item { 
            text-decoration: none; color: inherit; border: 1px solid var(--accent-dim); 
            padding: 1.5rem; transition: 0.3s; position: relative;
        }
        .doc-item:hover { border-color: var(--accent); transform: scale(1.02); background: #f9faff; }
        .doc-num { font-size: 0.65rem; color: var(--accent); margin-bottom: 0.5rem; }
        .doc-title { font-size: 1rem; font-weight: 500; margin-bottom: 0.5rem; }
        .doc-sub { font-size: 0.75rem; color: var(--text-dim); }
        .doc-arrow { position: absolute; right: 1.5rem; bottom: 1.5rem; color: var(--accent); opacity: 0; transition: 0.3s; }
        .doc-item:hover .doc-arrow { opacity: 1; }

        /* MODO SOMBRA BUTTON */
        .sombra-access {
            display: inline-block; margin-top: 4rem; padding: 1rem 2rem;
            background: #000; color: #ffbf00; border: 1px solid #ffbf00;
            text-decoration: none; font-size: 0.8rem;
        }

        .section-divider {
            grid-column: 1 / -1; font-size: 0.7rem; text-transform: uppercase;
            border-bottom: 1px solid var(--accent-dim); padding-bottom: 0.5rem;
            margin-top: 3rem; display: flex; justify-content: space-between;
        }
    </style>
</head>
<body class="status-low" id="main-body">

<div class="doc-container">
    
    <div class="metrics-header">
        <div class="scorecard">
            <div class="label">NTI GLOBAL</div>
            <div class="val" id="nti-val">45.2</div>
        </div>
        <div class="scorecard">
            <div class="label">IHG (ÍNDICE)</div>
            <div class="val">0.82</div>
        </div>
        <div class="scorecard">
            <div class="label">MONTECARLO_VAR</div>
            <div class="val" id="var-val">±2.4%</div>
        </div>
    </div>

    <div class="doc-label">Punto de entrada</div>
    <h1>Documentos sobre<br>fricción sistémica.<br>Cada uno diseñado<br>para extraerse.</h1>

    <div class="ecg-box">
        <div class="ecg-line" id="ecg"></div>
    </div>

    <p>Este repositorio no prescribe soluciones. Describe patrones.<br>El uso es responsabilidad de quien lee.</p>

    <div class="rule"></div>

    <div class="section-divider">System Friction · núcleo operativo <span>v1.0</span></div>
    
    <div class="doc-grid">
        <a href="docs/core-00.md" class="doc-item">
            <div class="doc-num">core-00 · META</div>
            <div class="doc-title">Cómo leer este ecosistema</div>
            <div class="doc-sub">Documento metodológico. Tono, progresión y límites del archivo.</div>
            <span class="doc-arrow">→</span>
        </a>
        <a href="docs/core-0.md" class="doc-item">
            <div class="doc-num">core-0 · POSICIÓN</div>
            <div class="doc-title">Desde dónde observa el observador</div>
            <span class="doc-arrow">→</span>
        </a>
    </div>

    <div class="section-divider">Serie aplicada · Nodo Aguascalientes <span>AGS01 – AGS06</span></div>
    <div class="doc-grid">
        <a href="data/ags/agua.json" class="doc-item" style="grid-column: 1 / -1; border-left: 5px solid var(--accent);">
            <div class="doc-num">DATOS EN TIEMPO REAL</div>
            <div class="doc-title">Aguascalientes como sistema observable</div>
            <div class="doc-sub">Métricas inyectadas desde 10,000 iteraciones Montecarlo.</div>
            <span class="doc-arrow">→</span>
        </a>
    </div>

    <a href="core/nodo_aptymok.md" class="sombra-access">
        IR AL NODO APTYMOK (SOMBRA) →
    </a>

</div>

<script>
    // LÓGICA DE MOVIMIENTO SEGÚN MÉTRICAS REALES
    const ntiData = [45.2, 48.9, 55.4, 72.1, 30.5, 66.8];
    let i = 0;

    function updateSystem() {
        const val = ntiData[i];
        const body = document.getElementById('main-body');
        document.getElementById('nti-val').innerText = val;
        
        // Cambio de color de fondo (Semáforo)
        body.className = '';
        if(val < 50) body.classList.add('status-low');
        else if(val < 70) body.classList.add('status-mid');
        else body.classList.add('status-high');

        // Efecto visual en el ECG (A mayor NTI, más vibración)
        const ecg = document.getElementById('ecg');
        ecg.style.height = (val / 10) + 'px';

        i = (i + 1) % ntiData.length;
    }

    setInterval(updateSystem, 3000); // Actualiza cada 3 segundos
</script>

</body>
</html>