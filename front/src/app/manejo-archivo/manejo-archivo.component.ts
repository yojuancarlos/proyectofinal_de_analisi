import { Component } from '@angular/core'
import { ArchivosService } from '../servicios/archivos.service'
import * as XLSX from 'xlsx'
import { FormGroup, FormControl } from '@angular/forms'
import { catchError, of, tap } from 'rxjs'


@Component({
  selector: 'app-manejo-archivo',
  templateUrl: './manejo-archivo.component.html',
  styleUrls: ['./manejo-archivo.component.css']
})
export class ManejoArchivoComponent {
  matrices: any[] = []
  archivo_enviado: boolean = false
  lista_resultados: string[] = []
  currentTableIndex: number = 0
  digit: string = ''
  emdMinima: number = 0
  particion: [string[], string[]] = [[''], ['']]

  constructor(private archivoService: ArchivosService) { }


  csvImport(event: any): void {
    const file = event.target.files[0]
    if (file) {
      this.archivoService.subirArchivo(file).pipe(
        tap(() => {
          this.archivo_enviado = true
          // Refresh file list or any other necessary state updates
        }),
        catchError(err => {
          console.error('Error al subir el archivo', err)
          return of(null) // Handle error without breaking the stream
        })
      ).subscribe()
    }
  }

  iterarSoluciones(): void {
    this.matrices = ['solucion_matriz_original.csv', 'solucion_matriz_dinamica.csv']
    this.matrices.forEach(resultado => {
      this.descargarYMostrarArchivo(resultado)
    })
  }

  descargarArchivo(filename: string): void {
    this.archivoService.descargarArchivo(filename)
      .subscribe(data => {
        const url = window.URL.createObjectURL(data)
        const a = document.createElement('a')
        a.href = url
        a.download = filename
        document.body.appendChild(a)
        a.click()
        window.URL.revokeObjectURL(url)
        a.remove()
      }, error => console.error('Error al descargar el archivo', error))
  }

  calcularYDescargar(): void {
    this.archivoService.calcularSolucion(this.digit).pipe(
      tap(res => {
        this.emdMinima = res.emd_minima
        this.particion = res.mejor_particion
        console.log('Solución calculada', res)
        console.log(res.emd_minima)
        console.log(res.mejor_particion)
        this.iterarSoluciones()
      }),
      catchError(err => {
        console.error('Error al calcular la solución', err)
        return of(null) // Handle error
      })
    ).subscribe()
  }



  descargarYMostrarArchivo(filename: string): void {
    if (!this.archivo_enviado) return

    this.archivoService.descargarArchivo(filename).subscribe(
      data => {
        const reader = new FileReader()
        reader.onload = (e: any) => {
          const ab = e.target.result
          const wb = XLSX.read(ab, { type: 'array' })
          const sheetName = wb.SheetNames[0]
          const worksheet = wb.Sheets[sheetName]
          this.matrices = XLSX.utils.sheet_to_json(worksheet, { header: 1 })
        }
        reader.readAsArrayBuffer(data)
      },
      error => console.error('Error al descargar el archivo', error)
    )
  }

  onDigitChange(value: string) {
    this.digit = String(value)
  }

  nextTable(): void {
    if (this.matrices.length > 0) {
      this.currentTableIndex = (this.currentTableIndex + 1) %
        this.matrices.length
      // this.descargarArchivo(this.matrices[this.currentTableIndex])
    }
  }

  previousTable(): void {
    if (this.matrices.length > 0) {
      this.currentTableIndex = (this.currentTableIndex +
        this.matrices.length - 1) % this.matrices.length
      // this.descargarArchivo(this.matrices[this.currentTableIndex])
    }
  }


  // calcularYDescargar() {
  //   this.archivoService.calcularSolucion(String(this.digit)).subscribe({
  //     next: (res) => {
  //       console.log('Solución calculada', res)
  //       console.log(res.emd_minima)
  //       console.log(res.mejor_particion)
  //       this.iterarSoluciones()
  //     },
  //     error: (error) => console.error('Error al calcular la solución', error)
  //   })
  // }
}
